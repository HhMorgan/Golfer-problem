int: weeks;
int: groups;
int: groupSize;
int: players = groups * groupSize;
 
set of int: Players = 1..players;
set of int: Weeks = 1..weeks;
set of int: Groups = 1..groups;
set of int: GroupSize = 1..groupSize;
set of int: Bool = 0..1;
array[Weeks,Groups,Players] of var Bool: assignments;
% All player play at most once every week
constraint forall(p in Players, w in Weeks) (
  sum(g in Groups) (bool2int(assignments[w,g,p] = 1)) = 1 
);
%All groups are exactly groupSize large
constraint forall(w in Weeks, g in Groups)(
  sum(p in Players) (bool2int(assignments[w,g,p] = 1)) = groupSize
);
%All player play together at most once
constraint forall(i,j in Players where i < j) (
  sum(w in Weeks, g in Groups) (bool2int(assignments[w,g,i] = 1 /\ assignments[w,g,j] = 1)) <= 1
);
solve satisfy;
