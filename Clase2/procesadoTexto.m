clear all, close all, clc
a = imread('texto.png');
b = rgb2gray(a);
figure; imshow(b); impixelinfo
c = b';
figure; imshow(c)
d = sum(c);
figure; plot(d)
e = b(10:40,:);
figure; imshow(e)
f = b(70:90,:);
figure; imshow(f)
g = sum(f);
figure; plot(g)
h = f(:,290:360);
figure; imshow(h)
i = sum(h);
figure; plot(i)
j = h(:,18:28);
figure; imshow(j)




