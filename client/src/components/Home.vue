<template>
  <div class="row">
    <div class="sm-6 md-8 lg-10 col">Hello</div>
    <aside class="paper sm-6 md-4 lg-2 col">
      <h3>Categories</h3>
      <input type="search" class="form-control" placeholder="e.g. filter" role="searchbox">
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
