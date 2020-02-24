function [acc,cost_all]=aml_patient(fold,lambda)
%[file,folder]=uigetfile;
%filename=fullfile(folder,file);
data=readmatrix("final7.csv");
X=data(:,[1:56]);
y=data(:,57);
[m,n] = size(X);
indices = crossvalind('Kfold',y,fold);
theta_avg=zeros(n+1,1);
cost_avg=zeros(fold,1);
accu_avg=zeros(fold,1);
for i=1:fold
test = (indices == i); train = ~test;
X_train=X(train,:);
X_test=X(test,:);
y_train=y(train,:);
y_test=y(test,:);
[theta,cost]=model(lambda,X_train,y_train);
p=predict(theta,X_test);
cost_avg(i)=cost;
p_avg=predict(theta,X_test);
acc_avg(i)=mean(double(p_avg == y_test)) * 100;
if(all(theta_avg,"all"))
    theta_avg=theta_avg+theta;
else
    theta_avg=theta;
end
end
theta_all=theta_avg./fold;
cost_all=mean(cost_avg);
acc=mean(acc_avg);
X_pred=readmatrix("testing_data.csv");
y_pred=predict(theta_all,X_pred);
writematrix(y_pred,"Pred.csv")
end
