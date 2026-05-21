// lista encadeada simulada
let valores = [];
let proximo = [];

let inicio = -1;
let ultimo = -1;

function adicionarFim() {
  let nome = document.getElementById('nome').value;
  if (nome === '') {
    alert('Digite um nome');
    return;
  }
  let novoIndice = valores.length;
  valores.push(nome);
  proximo.push(-1);

  if (inicio === -1) {
    inicio = novoIndice;
    ultimo = novoIndice;
  } else {
    proximo[ultimo] = novoIndice;
    ultimo = novoIndice;
  }

  document.getElementById('nome').value = '';
  alert('Elemento adicionado');
  mostrar();
}

function adicionarInicio() {
  let nome = document.getElementById('nome').value;
  if (nome === '') {
    alert('Digite um nome');
    return;
  }
  let novoIndice = valores.length;
  valores.push(nome);
  // novo aponta para o antigo inicio
  proximo.push(inicio);
  // novo vira inicio
  inicio = novoIndice;
  // se era vazia
  if (ultimo === -1) {
    ultimo = novoIndice;
  }
  document.getElementById('nome').value = '';
  alert('Elemento adicionado');
  mostrar();
}
function removerInicio() {
  if (inicio === -1) {
    alert('Lista vazia');
    return;
  }
  // inicio passa a ser o próximo
  inicio = proximo[inicio];

  // se ficou vazia
  if (inicio === -1) {
    ultimo = -1;
  }
  mostrar();
}
function contar() {
  let quantidade = 0;
  let atual = inicio;
  while (atual !== -1) {
    quantidade++;
    atual = proximo[atual];
  }
  document.getElementById('saida').innerHTML =
    'Quantidade de elementos: ' + quantidade;
}
function deletar() {
  let nome = document.getElementById('nome').value;
  if (nome === '') {
    alert('Digite um nome');
    return;
  }

  let atual = inicio;
  let anterior = -1;

  while (atual !== -1) {
    if (valores[atual] === nome) {
      if (anterior === -1) {
        inicio = proximo[atual];
      } else {
        proximo[anterior] = proximo[atual];
      }
      if (proximo[atual] === -1) {
        ultimo = anterior;
      }
      mostrar();
      return;
    }
    anterior = atual;
    atual = proximo[atual];
  }

  alert('Nome não encontrado');
}

function mostrar() {
  let resultado = '';
  let atual = inicio;

  while (atual !== -1) {
    resultado += valores[atual] + ' → ';
    atual = proximo[atual];
  }

  if (inicio === -1) {
    resultado = 'Lista vazia';
  } else {
    resultado += 'FIM';
  }

  document.getElementById('saida').innerHTML = resultado;
}

window.onload = mostrar;
