clear all, close all, clc
a=imread("figuras.bmp"); %a=im2bw(a,0.5);
figure;imshow(a);impixelinfo
[l,n]=bwlabel(a);l1=uint8(l);l1=normalize(l1);
figure;imagesc(l);colormap(cool);impixelinfo
title(['# objetos = ', num2str(n)])
figure;imshow(l1);impixelinfo