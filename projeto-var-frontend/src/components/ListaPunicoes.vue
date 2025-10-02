<template>
  <div class="container">
    <h1>Painel de Punições VAR</h1>
    
    <div v-if="loading">
      Carregando dados da API...
    </div>

    <div v-else-if="error" class="error">
      Erro: {{ error }}
    </div>

    <div v-else>
      <h2>Punições Recentes (Total: {{ punicoes.length }})</h2>
      
      <table>
        <thead>
          <tr>
            <th>ID Punido</th>
            <th>ID Discord</th>
            <th>Motivo</th>
            <th>VAR Responsável</th>
            <th>Tempo (dias)</th>
            <th>Data</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="punicao in punicoes" :key="punicao.id">
            <td>{{ punicao.id_punido }}</td>
            <td>{{ punicao.id_dc }}</td>
            <td>{{ punicao.motivo_nome }}</td>
            <td>{{ punicao.nick_name_nome }}</td>
            <td>{{ punicao.temp_ban }}</td>
            <td>{{ formatDate(punicao.created) }}</td>
            <td><a :href="punicao.link_evid" target="_blank">Ver Prova</a></td>
          </tr>
        </tbody>
      </table>
      
      <h3>Motivos Cadastrados:</h3>
      <ul>
        <li v-for="motivo in motivos" :key="motivo.id">{{ motivo.nome }}</li>
      </ul>
      
      <h3>VARs Cadastrados:</h3>
      <ul>
        <li v-for="varItem in vares" :key="varItem.id">{{ varItem.nome }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

// URL base da sua API Django (Certifique-se de que o Django está rodando em http://localhost:8000)
const API_BASE_URL = 'http://localhost:8000/punicao/api/';

export default {
  name: 'ListaPunicoes',
  data() {
    return {
      punicoes: [],
      motivos: [],
      vares: [],
      loading: true,
      error: null,
    }
  },
  methods: {
    formatDate(isoDate) {
      if (!isoDate) return 'N/A';
      return new Date(isoDate).toLocaleDateString('pt-BR');
    },
    async fetchData() {
      this.loading = true;
      try {
        // 1. Busca Punições
        const punicoesResponse = await axios.get(API_BASE_URL + 'punicoes/');
        this.punicoes = punicoesResponse.data;

        // 2. Busca Motivos
        const motivosResponse = await axios.get(API_BASE_URL + 'motivos/');
        this.motivos = motivosResponse.data;

        // 3. Busca Vares
        const varesResponse = await axios.get(API_BASE_URL + 'vares/');
        this.vares = varesResponse.data;

      } catch (error) {
        console.error("Erro ao carregar dados da API:", error);
        // O erro pode ser causado por CORS (se não tiver configurado corretamente no Django)
        this.error = "Não foi possível conectar ou carregar dados da API. Verifique se o Django está rodando e se o CORS está configurado (Django Rest Framework + django-cors-headers).";
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    // Chamada inicial para buscar os dados quando o componente é montado
    this.fetchData();
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #f2f2f2;
}
.error {
  color: red;
  font-weight: bold;
}
</style>