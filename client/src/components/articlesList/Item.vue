<template>
  <div class="card" style="width:100%;">
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <h5 class="card-subtitle">Written by {{ author.username }}</h5>
      <h5 class="card-subtitle">Posted on {{ publishedAt }}</h5>
      <div class="btn">
        <button>
          <router-link :to="{ name: 'article', params: { articleID: id }}">Let me go here!</router-link>
        </button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.card {
  margin-bottom: 1rem;
}
.btn {
  display: flex;
  justify-content: flex-end;
}
</style>

<script>
export default {
  name: "Article-item",
  props: ["id", "title", "publishedAt", "author", "category"],
  data() {
    return {};
  }
};
</script>