clear all, close all, clc;
cb = imread('cb.jpg');
cs = imread('cs.jpg');
figure; imshow([cb, cs]); impixelinfo
a = imread('carro (1).jpg');
l = graythresh(cb);
b = im2bw(cb, l + 0.5); b = normalize(b);
figure; imshow(b)
c = cat(3, b,b,b);
d = a;
d(c == 0) = 0;
figure;imshow([a,d])