🚚 Rota Inteligente: Otimização de Entregas com Algoritmos de IA

📌 Sobre o Projeto
Este projeto foi desenvolvido como uma solução inteligente para otimizar a gestão de entregas da empresa de delivery de alimentos "Sabor Express" 🍝🍲🍔. A iniciativa surge como resposta ao desafio de gerenciar eficientemente as entregas durante horários de pico ⏰, que resultavam em rotas ineficientes, atrasos e insatisfação dos clientes 😞.
A solução proposta utiliza algoritmos de Inteligência Artificial 🤖🌐 para sugerir as rotas mais eficientes para os entregadores. O problema foi modelado como um grafo 🗺️, onde os pontos de entrega são representados por nós e as ruas por arestas, com pesos baseados em distância ou tempo.
![Gráfico de Otimização de Rotas](https://github.com/Tatysketch/Rota-inteligente-otimizacao-IA/blob/main/Grafico_Rotasdeentregas.png)

⚙️ Funcionalidades
- Otimização de Rotas: Aplicação de algoritmos de busca (como A*, busca em largura/profundidade) para encontrar o menor caminho entre múltiplos pontos de entrega 🧭.
- Agrupamento Inteligente: Implementação de algoritmos de clustering (como K-Means) para agrupar entregas próximas 📦, otimizando o trabalho dos entregadores e reduzindo o tempo de percurso ⏳.
- Redução de Custos: A otimização de rotas contribui diretamente para a redução do consumo de combustível ⛽ e dos custos operacionais 💰.
- Melhora na Experiência do Cliente: Entregas mais rápidas e eficientes aumentam a satisfação do cliente 😊 e a competitividade da empresa 📈.

🎯 Estratégias de Otimização e Contingência (Bônus)
Em um cenário real, a otimização de rotas deve ser dinâmica e resiliente 💡. Para garantir a máxima eficiência e a satisfação do cliente, o projeto propõe as seguintes estratégias adicionais:
- Otimização Dinâmica e Rotas de Atalho: A solução vai além da rota estática. A estratégia de bônus incorpora a criação de "rotas ponte" ou rotas de atalho estratégicas 🚦 que, ao considerar dados de trânsito em tempo real (como horários de pico), permitem desviar de congestionamentos 🚗🚕🚙. Isso garante a redução do tempo de entrega e aumenta a satisfação do cliente, transformando dados dinâmicos em decisões operacionais eficientes 📊.
- Gestão de Contingência com Equipe Flexível: Para mitigar riscos ⚠️ e garantir a continuidade do serviço, a estratégia inclui a alocação de recursos de contingência:
- Motoristas Freelancer: A contratação de três motoristas freelancer 🚐 para rotas atípicas ou de longa distância (como entre São Paulo e Juquitiba). Esta abordagem minimiza custos fixos e é acionada somente em casos específicos, sem afetar o investimento em veículos da frota principal 🚛.
- Adaptação Veicular: Em condições climáticas adversas 🌧️, como chuva, veículos adicionais (carros) podem ser acionados para suprir a demanda e manter a segurança e a velocidade das entregas 🛞, garantindo que o serviço não seja interrompido.
- Agentes de Backup: Dois agentes de backup 🧑‍🔧 são mantidos prontos para intervir em imprevistos menores, como um pneu furado ou outro problema mecânico 🔧, garantindo que a entrega seja concluída sem atrasos significativos.

### 🧠 Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias e conceitos de IA:

* **Python** 🐍: Linguagem de programação principal.
* **Teoria de Grafos** 🕸️: Para representar o problema de rotas e encontrar o caminho ideal. O algoritmo de **Dijkstra** foi usado para encontrar o caminho mais curto.
* **Aprendizado Não Supervisionado** 🧬: Algoritmo **K-Means** para o agrupamento de entregas.
[ROTAS DE ENTREGAS](https://github.com/Tatysketch/Rota-inteligente-otimizacao-IA/blob/main/ROTAS-otimiza%C3%A7%C3%A3o.png?raw=true)

### 💻 Como Usar
Para executar o projeto localmente, siga os seguintes passos:

1.  Clone o repositório para a sua máquina local:
    ```bash
    git clone [https://github.com/Tatysketch/Rota-inteligente-otimizacao-ia](https://github.com/Tatysketch/Rota-inteligente-otimizacao-ia)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd Rota-inteligente-otimizacao-ia
    ```
3.  Instale as bibliotecas necessárias:
    ```bash
    pip install pandas scikit-learn matplotlib networkx
    ```
4.  Execute o script principal para visualizar a otimização das rotas:
    ```bash
    python src/main.py
    ```
5. 💙🖋️ Autoria

Autor(a): Tatielle Pereira Dias Troto 💻✨

Disciplina: Artificial Intelligence Fundamentals 🧠📊
