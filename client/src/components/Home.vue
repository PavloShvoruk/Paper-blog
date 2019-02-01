<template>
  <div class="row">
    <aside class="sm-12 md-3 col sidebar">
      <div class="paper">
        <h3>Categories</h3>
        <input type="search" class="form-control" placeholder="e.g. filter" role="searchbox">
        <categoriesList :categories="categories"/>
      </div>
    </aside>
    <div class="sm-12 md-5 col">
      <articleList :articles="articles"/>
    </div>
  </div>
</template>

<style scoped>
.row {
  margin-top: 5rem;
}
.paper {
  width: auto;
  text-align: center;
}

.form-control {
  width: 100%;
}
</style>

<script>
import ApiService from "../ApiService.js";
import categoriesList from "../components/categoriesList/List";
import articleList from "../components/articlesList/List";
export default {
  components: {
    categoriesList,
    articleList
  },
  name: "home",
  data() {
    return {
      categories: [],
      articles: []
    };
  },
  async mounted() {
    try {
      this.categories = await ApiService.getCategories();
      this.articles = await ApiService.getArticles();
    } catch (error) {
      console.log(error.message);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
