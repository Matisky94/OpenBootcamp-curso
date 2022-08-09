public class Main {
    public static void main(String[] args) {
        System.out.println("------------------");
        int numeroIf = -5;
        if (numeroIf > 0) {
            System.out.println("El numero es positivo");
        } else if (numeroIf < 0) {
            System.out.println("El numero es negativo");
        } else {
            System.out.println("El numero es 0");
        }
        System.out.println("------------------");
        int numeroWhile = 0;
        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }
        System.out.println("------------------");
        do {System.out.println(numeroWhile);
        } while (numeroWhile < 3);
        System.out.println("------------------");
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println(numeroFor);
        }
        System.out.println("------------------");
        String estacion = "verano";
        switch (estacion){
            case "invierno": System.out.println("La estacion es invierno");
                break;
            case "primavera": System.out.println("La estacion es primavera");
                break;
            case "verano": System.out.println("La estacion es verano");
                break;
            case "otonio": System.out.println("La estacion es otonio");
                break;
            default: System.out.println("Error, la palabra ingresada no corresponde a una estacion");
        }

    }
}
