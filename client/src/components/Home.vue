<template>
  <div class="row">
    <div class="sm-12 md-8 col">Hello</div>
    <aside class="sm-12 md-4 col sidebar">
      <categoriesList :categories="categories"/>
    </aside>
  </div>
</template>

<script>
import ApiService from "../ApiService.js";
import categoriesList from "../components/categoriesList/List";
export default {
  components: {
    categoriesList
  },
  name: "home",
  data() {
    return {
      categories: []
    };
  },
  async mounted() {
    try {
      this.categories = await ApiService.getCategories();
    } catch (error) {
      console.log(error);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
