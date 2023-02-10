<template>
  <div class="row">
    <div class="col-md-12">
      <h3>Drift</h3>
    </div>
    <div class="col-md-12">
      <ul class="list-group">
        <li
          v-for="(fact, index) in catFacts"
          :key="index"
          class="list-group-item"
        >
          {{ index + 1 }}. {{ fact.text }}
        </li>
      </ul>
    </div>
    <div>
      <h1>POST response message</h1>
      <h2>{{ articleId }}</h2>
    </div>
    <div>
      <h1>GET data</h1>
      <h2>{{ totalVuePackages }}</h2>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
interface AnimalFacts {
  text: string;
}
export default defineComponent({
  name: "AnimalFacts",
  data() {
    return {
      catFacts: [] as AnimalFacts[],
      fetchingFacts: false,
      articleId: null,
      totalVuePackages: null,
    };
  },
  methods: {
    async POST() {
      const article = { title: "POST test" };
      const response = await axios.post(
        "https://reqres.in/api/articles",
        article
      );
      this.articleId = response.data;
    },

    async fetchCatFacts() {
      const catFactsResponse = await axios.get<AnimalFacts[]>(
        "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5"
      );
      this.catFacts = catFactsResponse.data;
    },

    async loadMoreFacts() {
      this.fetchingFacts = true;
      const catFactsResponse = await axios.get<AnimalFacts[]>(
        "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5"
      );
      this.catFacts.push(...(catFactsResponse.data || []));

      this.fetchingFacts = false;
    },

    async GET() {
      const response = await axios.get("https://api.npms.io/v2/search?q=vue");
      this.totalVuePackages = response.data.total;
    },
  },
  async mounted() {
    /*  await this.fetchCatFacts(); */
    await this.POST();
    await this.GET();
  },
});
</script>
