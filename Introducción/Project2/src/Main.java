public class Main {
    public static void main (String[] args){
        int total = suma(10, 15, 5);
        System.out.println(total);
        coche miCoche = new coche();
        miCoche.sumarPuertas();
        System.out.println(miCoche.puertas);
    }
    public static int suma(int a, int b, int c){
        return a + b + c;
    }
}

class coche{
    public int puertas = 2;
    public void sumarPuertas(){
        this.puertas++;
    }
}

