from clp import ClientOPC, ServerTCP
from tcp_client import tcp_client
from tanque import TanqueConico
from multiprocessing import Process


def main():
    open('MES.txt', 'w').close()

    client_opc_thread = ClientOPC()
    server_tcp_thread = ServerTCP()
    tanque_conico_thread = TanqueConico()

    href = input("Insira o setpoint de altura do tanque (Deve ser menor que a altura máxima especificada): ")

    tcp_client_process = Process(target=tcp_client, args=[href])
    
    server_tcp_thread.start()
    tcp_client_process.start()
    tanque_conico_thread.start()
    client_opc_thread.start()
    

    client_opc_thread.join()
    tanque_conico_thread.join()
    server_tcp_thread.join()
    tcp_client_process.terminate()

    print("Fim do ciclo de controle")

if __name__ == "__main__":
    main()