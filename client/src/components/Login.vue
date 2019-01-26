<template>
  <div>
    <fieldset class="form-group">
      <legend>Some Check Boxes</legend>
      <label for="paperChecks1" class="paper-check">
        <input type="checkbox" name="paperChecks" id="paperChecks1" value="option 1">
        <span>This is the first check</span>
      </label>
      <label for="paperChecks2" class="paper-check">
        <input type="checkbox" name="paperChecks" id="paperChecks2" value="option 2">
        <span>This is the second check</span>
      </label>
    </fieldset>
  </div>
</template>

<script>
export default {
  name: "login"
};
</script>