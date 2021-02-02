package DinamicProgramming;
/*
* given  coins ={2,5,7} get amount 27 calculate the min coins
*/
public class CoinsChange {
    public int coins( int[] A, int M){
        /* store status*/
        int[] f = new int[M+1];
        /* initialization*/
        f[0] = 0 ;
        for(int i =1;i<M+1;i++){
            /* set f[i] to maxinteger which is useful in future use*/
            f[i] = Integer.MAX_VALUE;
            for(int j = 0;j<A.length;j++){
                /* last coin A[j]*/
                /* boundary*/
                if(i-A[j]>=0 && f[i-A[j]]!= Integer.MAX_VALUE){
                    f[i] = Math.min(f[i-A[j]]+1,f[i]);
                }

            }
        }
        if(f[M] == Integer.MAX_VALUE){
            f[M] = -1;
        }
        return f[M];
    }

}
