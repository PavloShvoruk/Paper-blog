<template>
  <div class="title">
    <h5>{{ name }}</h5>
  </div>
</template>
<style scoped>
.title {
  cursor: pointer;
}
</style>

<script>
export default {
  name: "category-item",
  props: ["name"]
};
</script>