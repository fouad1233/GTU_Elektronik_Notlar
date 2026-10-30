function [pabs, pangle] = rectangulartopolar(rect)
%UNTİTLED Summary of this function goes here
%   Detailed explanation goes here
pabs = abs(rect);
pangle = angle(rect).*180./pi;

end

