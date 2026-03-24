public class paciente{
    String nombre;
    String fecha;
    int semana;
    int temperatura;
    boolean fiebre;


        public paciente(){}
        public void SetNombre(String n){
            nombre = n;
        }
        public void SetFecha(String f){
            fecha = f;
        }
        public void SetSemana(int s){
            semana = s;
        }
        public void SetTemperatura(int t){
            temperatura = t;
        }
        public String GetNombre(){
            return nombre;
        }
        public String GetFecha(){
            return fecha;
        }
        public int getTemperatura(){
            return temperatura;
        }
        public int GetSemnana(){
            return semana;
        }
        public void MostrarInformacion(){
            System.out.println("########### informacion del paciente ########### ");
            System.out.println("Nombre del paciente: "+nombre);
            System.out.println("Fecha de nacimiento: "+fecha);
            System.out.println("Semanas de gestacion de la paciente: "+semana);
            System.out.println("Temperatura del dia: "+temperatura);
        }



}