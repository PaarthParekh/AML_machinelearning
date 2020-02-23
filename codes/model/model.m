function [theta, cost] = model(lambda,X_training,y_training)
[m_training,n_training]=size(X_training);
X_training=[ones(m_training,1),X_training];
initial_theta=zeros(n_training+1,1);
[J,grad]=costFunctionReg(initial_theta,X_training,y_training,lambda);
fprintf("Initial cost:%f\n",J)
options = optimset('GradObj', 'on', 'MaxIter', 800);
[theta, cost] = fminunc(@(t)(costFunctionReg(t, X_training, y_training,lambda)), initial_theta, options);
end
