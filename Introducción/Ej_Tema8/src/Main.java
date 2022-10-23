public class Main {
    public static void main(String[] args) {
        persona persona1 = new persona();
        persona1.setEdad(25);
        persona1.setNombre("Marcos");
        persona1.setTelefono(54451875);
        System.out.println(persona1.getNombre());
        System.out.println(persona1.getEdad());
        System.out.println(persona1.getTelefono());
    }
}

class persona{
    private int edad;
    private int telefono;
    private String nombre;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getTelefono() {
        return this.telefono;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }
}
