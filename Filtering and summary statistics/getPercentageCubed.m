function [ counts ] = getPercentageCubed( mat,epsilon )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

lengths = size(mat,2)-sum(isnan(mat),2)-sum((mat<0),2);
mat(isnan(mat))=3;
mat(mat<0)=3;
p=(mod(mat.^(1/3), 1))<epsilon;
percentages = sum(p,2)./lengths*100;
h = histogram(percentages,(0:1:100));
title('percentage of cubed in series');
xlabel('percentage of cubed');
counts = h.Values;
saveas(gcf,'CubedPercent.png');


end