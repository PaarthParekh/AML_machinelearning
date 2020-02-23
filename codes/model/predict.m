function p = predict(theta, X)
[m,n]=size(X);
X=[ones(m,1),X];
pred=sigmoid(X*theta);
p=pred>=0.5;
end
