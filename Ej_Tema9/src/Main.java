public class Main {
    public static void main(String[] args) {
        Cliente client1 = new Cliente();
        client1.nombre = "Fulanito";
        client1.edad = 32;
        client1.telefono = 15567845;
        client1.credito = 20000;
        System.out.println("El nombre del cliente es: " + client1.nombre);
        System.out.println("Su edad es: " + client1.edad);
        System.out.println("Su telefono es: " + client1.telefono);
        System.out.println("El credito del que dispone es: " + client1.credito);
        System.out.println("-------------------------");
        Trabajador trabajador1 = new Trabajador();
        trabajador1.nombre = "Menganito";
        trabajador1.edad = 27;
        trabajador1.telefono = 15593271;
        trabajador1.salario = 5000;
        System.out.println("El nombre del trabajador es: " + trabajador1.nombre);
        System.out.println("Su edad es: " + trabajador1.edad);
        System.out.println("Su telefono es: " + trabajador1.telefono);
        System.out.println("El salario del que dispone es: " + trabajador1.salario);
    }
}

class Persona{
    String nombre;
    int edad;
    int telefono;
}

class Cliente extends Persona{
    int credito;
}

class Trabajador extends Persona{
    int salario;
}