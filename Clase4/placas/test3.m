clear all; close all; clc
a=imread("placa_bin.bmp");
[l,n]=bwlabel(a);
figure;imagesc(l);impixelinfo
title(['Hay ', num2str(n), ' objetos']);
total=[];
for i=1:n
    b=a*0;
    b(l==i)=255;area=sum(b(:))/255;total=[total,area];
    %figure(4);imshow(b);title(['obj ', num2str(i)])
    %pause
end
figure;plot(total)
b=a*0;b(l==155)=255;
figure;imshow(b)
[fil,col]=find(b>0);
fmin=min(fil);fmax=max(fil);
cmin=min(col);cmax=max(col);
a=imread("carro (1).jpg");
%%
b=a(fmin:fmax,cmin:cmax,:);
figure;imshow(b)
