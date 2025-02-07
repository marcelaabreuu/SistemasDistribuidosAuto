# Trabalho Prático Final

## Descrição do Projeto

Este projeto tem como objetivo controlar e monitorar o nível de líquido em um tanque industrial, garantindo que ele não ultrapasse o limite máximo nem fique abaixo do nível desejado. Para isso, foi desenvolvida uma arquitetura que envolve a comunicação entre um cliente e um servidor TCP, que se conecta a um cliente e servidor OPC. O cliente OPC simula o comportamento do tanque, controlando o enchimento e o esvaziamento.

---

## Especificações do Tanque

- **Altura máxima:** 5.0 metros  
- **Raio da entrada (Raio 0):** 1.0 metro  
- **Raio da saída (Raio 1):** 2.0 metros  
- **Coeficiente de descarga da saída:** 1.2  

---

## Estrutura do Projeto

O projeto está organizado em vários arquivos, cada um responsável por uma parte específica do sistema. Abaixo está a descrição de cada um:

### 1. **tanque_conico**
   - É a thread que simula o comportamento do tanque cônico.  
   - Atua como um cliente OPC, enviando e recebendo dados do servidor OPC.  
   - Controla o enchimento do tanque com base nas informações recebidas.

### 2. **clp**
   - Contém duas threads principais:  
     - **ClientOPC:** Controla a vazão de entrada do líquido no tanque com base na altura atual (recebida do servidor OPC) e na altura de referência (enviada pelo servidor TCP).  
     - **ServerTCP:** Recebe a altura de referência do cliente TCP e envia a altura atual do líquido (recebida do cliente OPC) via socket.  

### 3. **tcp_client**
   - É um processo que se comunica com o servidor TCP/IP via socket.  
   - Armazena os valores da altura do líquido em um arquivo chamado "historiador".  
   - Envia a altura de referência para o servidor TCP.  
   - Escreve os dados no arquivo `data.txt`, que é usado para gerar o gráfico em tempo real.  
   - Exibe alertas no terminal caso o nível do líquido esteja fora do esperado.  
   - **Observação:** É recomendado excluir o arquivo "historiador" após cada execução, pois ele pode ficar muito grande devido ao grande volume de dados.

### 4. **timer**
   - É um dispositivo que executa tarefas repetidamente em intervalos de tempo definidos.  
   - Recebe como argumentos o intervalo de tempo e a função que será executada (chamada de "callback").

### 5. **main**
   - É o processo principal do projeto.  
   - Responsável por iniciar e encerrar as threads e processos.  

---

## Instalação das Dependências

Para rodar o projeto, é necessário instalar as bibliotecas utilizadas. A principal biblioteca é a `opcua`, que permite a comunicação com o servidor OPC. Para instalar todas as dependências de uma vez, basta executar o seguinte comando no terminal:

```bash
pip install -r requirements.txt