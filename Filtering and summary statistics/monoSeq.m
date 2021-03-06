%check for any monotonic sequences

function monoSeq(seqID)

if nargin == 1
	cleaned_data=getSeq(seqID);
else
	load cleaned_data;
end

vec_check_nonincreasing=zeros(1,size(cleaned_data,1));
vec_check_nondecreasing=zeros(1,size(cleaned_data,1));

%nondecreasing
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,:);
    if all(diff(seq(1:idx-1)) >=0)==1
       vec_check_nondecreasing(index)=i;
       index=index+1;
    end
end

[~,idx]=min(vec_check_nondecreasing);
vec_check_nondecreasing=vec_check_nondecreasing(1:idx-1);
nondecreasingMat=cleaned_data(vec_check_nondecreasing,:);
save('nondecreasingSeqData','nondecreasingMat')

%nonincreasing
index=1;
for i=1:size(cleaned_data,1)
    temp=isnan(cleaned_data(i,:)); %run over the seq till the NaN
    [~,idx]=max(temp);
    seq=cleaned_data(i,:);
    if all(diff(seq(1:idx-1)) <=0)==1
       vec_check_nonincreasing(index)=i;
       index=index+1;
    end
end

[~,idx]=min(vec_check_nonincreasing);
vec_check_nonincreasing=vec_check_nonincreasing(1:idx-1);
nonincreasingMat=cleaned_data(vec_check_nonincreasing,:);
save('nonincreasingSeqData','nonincreasingMat')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

nonMonotonic=size(cleaned_data,1)-size(nondecreasingMat,1)-size(nonincreasingMat,1);

fprintf('number of nondecreasing seq:%d\n',size(nondecreasingMat,1));
fprintf('number of nonincreasing seq:%d\n',size(nonincreasingMat,1));
fprintf('number of nonMonotonic seq:%d\n',nonMonotonic);

end