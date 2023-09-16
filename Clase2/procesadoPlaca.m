clear all; close all; clc;
a = imread('placa.jpg');
b = rgb2gray(a);
b1 = imadjust(b);
figure, imshow([b,b1])
c = graythresh(b1);
% Binarizar las imagens
d = uint8(~im2bw(b1,c))*255;
figure, imshow(d)
e = d';
f = sum(e);
figure; plot(f)
% Extraer todas las letras de la placa
g = d(80:290,:);
figure; imshow(g)
h = sum(g);
figure; plot(h)
% Extraer letra de placa
i = g(:,170:280);
figure; imshow(i)

