
public class TarefaIncremento implements Runnable {
    private Contador contador;

    public TarefaIncremento(Contador contador) {
        this.contador = contador;
    }

    @Override
    public void run() {
        for(int i = 5; i < 100; i++) {
            contador.incrementar();
        }
    }
}
