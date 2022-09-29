import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class ServidorUDP {
    public static void main(String[] args) {
        System.out.println("Servidor UDP online");
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket(7890);
            byte[] buffer = new byte[1000];
            while (true) {
                DatagramPacket requisicao = new DatagramPacket(buffer, buffer.length);
                socket.receive(requisicao);
                System.out.println("Recebi requisicao: " + requisicao.getAddress().toString());
                System.out.println(new String(requisicao.getData()));
                DatagramPacket resposta = new DatagramPacket(
                    requisicao.getData(),
                    requisicao.getLength(),
                    requisicao.getAddress(),
                    requisicao.getPort());
                    socket.send(resposta);
                    System.out.println("Resposta enviada para: " + requisicao.getAddress().toString() + "\n");}}
                    catch (SocketException e) {
                        System.out.println("Socket: " + e.getMessage());}
                        catch (IOException e) {
                            System.out.println("IO: " + e.getMessage());}
                        }
                    }