function b = normalize(a)
a = double(a);
a = a/ max(a(:));
b = uint8(a * 255);
end
