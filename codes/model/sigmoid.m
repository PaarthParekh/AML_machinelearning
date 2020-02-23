function g = sigmoid(z)
g = zeros(size(z));
d=zeros(size(z));
d=1+exp(-z);
g=rdivide(1,d);
end
