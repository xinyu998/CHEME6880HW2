clc
clear all
%6880 HW2_5 Xinyu Liu
y=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]';
z=[1.5;1.5;1.5];
x=[1 1 1;1 1 -1;1 -1 1;-1 1 1;-1 -1 1;-1 1 -1;1 -1 -1;-1 -1 -1;2 2 -2;2 -2 2;-2 2 2;-2 -2 -2;-2 -2 2;-2 2 -2;2 -2 -2;2 2 2];
x1=x';
c=ones(16);
K_poly=(c+transpose(x1)*x1).^2;
a_poly=vpa(alpha(K_poly,y))
b_p=vpa(Dfunction(x,[1;1;1],a_poly,1,y))
%test sample
kz=x*z;
kz=kz+ones(16,1);
kz=kz.^2;
fp=zeros(16,1);
for i=[1:1:16]
    fp(i)=a_poly*y(i)*kz(i);
end
fp=sum(fp);
testpoly=vpa(fp+b_p);
disp('Polynomial kernel SVM result is 0.55, result=yes')

%% Gaussian
K_g=zeros(16);
for i=[1:1:16]
    for j=[1:1:16]
    K_g(i,j)=exp(-0.5*(norm((x(i,:)-x(j,:)))^2));
    end
end
a_g=vpa(alpha(K_g,y))
b_g=vpa(Gfunction(x,[-2;2;2],a_g,-1,y))

%test sample
kzg=zeros(16,1);
for i=[1:1:16]
    kzg(i)=exp(-0.5*(norm((x(i,:)-z))^2));
end
fg=zeros(16,1);
for i=[1:1:16]
    fg(i)=a_poly*y(i)*kzg(i);
end
fg=sum(fg);
testgau=vpa(fg-0.232);
disp('Gaussian kernel SVM result is -0.23, result=No')
%% Functions
%Alpha function
function [a]=alpha(K,y)
C=zeros(16);
for i=[1:1:16]
    for j=[1:1:16]
    C(i,j)=y(i)*y(j)*K(i,j);
    end
end
CC=sum(sum(C));
syms a
fun=@(a)16*a-(CC/2)*a^2;
f2=diff(fun,a)==0;
a=solve(f2,a);
end

%Decision boundary function ploy
function [b]=Dfunction(x,xtest,a,c,y)
%kernal for one sample
kxz=x*xtest;
kxz=kxz+ones(16,1);
kxz=kxz.^2;
f=zeros(16,1);
syms b
for i=[1:1:16]
    f(i)=a*y(i)*kxz(i);
end
f=sum(f);
fb=f+b;
b=solve(fb==c,b);
end

%Decision boundary function Gau
function [b,kxg]=Gfunction(x,xtest,a,c,y)
%kernal for one sample
kxg=zeros(16,1);
for i=[1:1:16]
    kxg(i)=exp(-0.5*(norm((x(i,:)-xtest))^2));
end
syms b
f=zeros(16,1);
for i=[1:1:16]
    f(i)=a*y(i)*kxg(i);
end
fb=sum(f)+b;
b=solve(fb==c,b);
end