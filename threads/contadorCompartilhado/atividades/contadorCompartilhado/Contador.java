package atividades.contadorCompartilhado;

public class Contador {
    private int valor = 0;

    public synchronized void incrementar() { // espaço de memória compartilhado
        valor++;
    }

    public int getValor() {
        return valor;
    }
}
