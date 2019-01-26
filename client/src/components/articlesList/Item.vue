<template>
  <div class="card" style="width:100%;">
    <div class="card-body">
      <h4 class="card-title">{{ title }}</h4>
      <h5 class="card-subtitle">{{ publishedAt }}, {{ author.username }}</h5>
      <p class="card-text">{{ articleText }}</p>
      <button>Let me go here!</button>
    </div>
  </div>
</template>
<style scoped>
.card {
  margin-bottom: 1rem;
}
</style>

<script>
export default {
  name: "Article-item",
  props: ["title", "articleText", "publishedAt", "author", "category"]
};
</script>