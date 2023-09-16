clear all, close all, clc
a = imread('imagen.jpeg');
a1 = a;
figure; imshow (a); impixelinfo
b = rgb2gray(a);
figure; imshow(b); impixelinfo
figure; imhist(b)
c = b;
c(c<50) = 0;
c(c>130) = 0;
d = c;
figure; imshow(c);
c(c>0) = 255;
figure; imshow([b,d,c]);
e = cat(3,c,c,c);
a(e==0) = 0;
figure; imshow(a);
f = b;
b(b<150)=0; b(b>200)=0; b(b>0)=255;
figure; imshow(b);
g = cat(3,b,b,b);
a1(g==0) = 0;
figure; imshow([f,b]);
figure; imshow(a1);
[fil,col,cap] = size(a);
area_total = fil*col
d(d>0) = 1;
area_l = sum(d(:))









