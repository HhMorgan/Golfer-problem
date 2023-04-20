include "alldifferent.mzn";
int: groupsNum;
int: groupSize;
int: weeksNum;
int: playersNum = groupsNum * groupSize;

set of int: Players = 1..playersNum;
set of int: Weeks = 1..weeksNum;
set of int: Groups = 1..groupsNum;
set of int: GroupSize = 1..groupSize;

%the symmetry constraint
predicate increasing3D(array[Weeks,Groups,GroupSize] of var Players: V) =
    forall(i in Weeks, j in Groups, k in 1..groupSize-1) (
        V[i,j,k] < V[i,j,k+1]
    );

%No two players can be present in two different groups in the same week
predicate allDiffFlattened(array[Weeks,Groups,GroupSize] of var Players: V) =  
    forall(i in Weeks) (
            alldifferent([V[i,j,k]| j in Groups, k in GroupSize])
        );
        
%assigning the beginning of the transpose of 2D array with the players of the first group in the first week  actual code: [i | i in 1..groupSize]
array[GroupSize] of Players:  assignmentForFirstGroupInFirstWeek = [i | i in 1..groupSize];
%assigning the players in the first week
array[Groups,GroupSize] of Players:  assignmentForFirstWeek = array2d(1..groupsNum,1..groupSize,[i | i in 1..playersNum]);

array[Weeks,Groups,GroupSize] of var Players: assignment;

constraint forall(i in Groups, j in GroupSize) (assignment[1,i,j] = assignmentForFirstWeek[i,j]);
constraint forall(i in 2..weeksNum, j in GroupSize) (assignment[i,j,1] = assignmentForFirstGroupInFirstWeek[j]);
constraint increasing3D(assignment);
constraint allDiffFlattened(assignment);
constraint forall(i in 1..weeksNum - 1, a in i+1..weeksNum, j,b in Groups)
(card(array2set([assignment[i,j,c] |  c in GroupSize]) intersect array2set([assignment[a,b,c] |  c in GroupSize])) <= 1);

solve satisfy;