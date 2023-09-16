clear all, close all, clc;
a = imread('carro (1).jpg');
figure; imshow(a);impixelinfo
b = rgb2hsv(a);
figure; imshow(b); impixelinfo
c = normalize(b);
figure; imshow(c); impixelinfo
d = rgb2lab(a);
figure; imshow(d); impixelinfo
e = normalize(d);
figure; imshow(e); impixelinfo
% RGB -> a, HSI -> c, LAB -> e
[c1, c2, c3] = componentes(a);
figure; imshow([c1, c2, c3]); impixelinfo
[c1, c2, c3] = componentes(b); cs = c2;
figure; imshow([c1, c2, c3]); impixelinfo
[c1, c2, c3] = componentes(e); cb = c3; cb=imadjust(cb);
figure; imshow([c1, c2, c3]); impixelinfo
figure; imshow(cs); impixelinfo
figure; imshow(cb); impixelinfo
imwrite(cb, 'cb.jpg');imwrite(cs, 'cs.jpg');
