function [J, grad] = costFunctionReg(theta, X, y, lambda)
m = length(y); % number of training examples

J = 0;
grad = zeros(size(theta));

rem_theta=theta(2:end,:);
pred=sigmoid(X*theta);
sub=1-pred;
error1=(-y.*log(pred))-((1-y).*log(sub));
square_theta=rem_theta'*rem_theta;
reg=(lambda/(2*m))*(sum(square_theta));
w_reg=(1/(m))*(sum(error1));
J=w_reg+reg;
fir_X=X(:,1);
rem_X=X(:,2:end);
grad_first=1/m*(sum((pred-y).*fir_X));
grad_reg=(lambda/m).*(rem_theta);
grad_rem=1/m*(sum((pred-y).*rem_X));
grad_fi=grad_rem+grad_reg';
grad=[grad_first,grad_fi];





% =============================================================

end
