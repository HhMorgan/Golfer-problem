package com.simplilearn.mavenproject;
import com.google.ortools.Loader;
import com.google.ortools.sat.BoolVar;
import com.google.ortools.sat.CpModel;
import com.google.ortools.sat.CpModelProto;
import com.google.ortools.sat.CpSolver;

public class NaiveGolferApproach {
	static {
		Loader.loadNativeLibraries();
	  }
     //Constants
    public static final int WEEKS = 10;
    public static final int PLAYERS = 32;
    public static final int GROUP_SIZE = 4;
    public static final int GROUPS_PER_WEEK = PLAYERS/GROUP_SIZE;
    public static void main(String[] args) {
        System.out.println( "Hello World!" );

        CpModel model = new CpModel();
        System.out.println( "Hello two!" );

       // CpSolver solver = new CpSolver();
        //CpModelProto.Builder builder = model.getBuilder();
        int assignments_size = WEEKS * GROUP_SIZE * PLAYERS;
        BoolVar[] assignments = new BoolVar[assignments_size];
//        HashMap<String, BoolVar> assignments = new HashMap<String, BoolVar>();
        for (int i = 0; i < PLAYERS; i++) {
            for (int j = 0; j < WEEKS; j++) {
                for (int k = 0; k < GROUP_SIZE; k++) {
                   String variable_name = "Player "+ i + ", " + " Week "+ j + " group "+ k;
                   BoolVar boolVar = model.newBoolVar(variable_name);
                   assignments[i+j+k] = boolVar;
                   System.out.println(variable_name);
//                    assignments.put(variable_name, new BoolVar(null, null, variable_name));
                }
            }
        }
    }
}