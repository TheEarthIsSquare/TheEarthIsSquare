<template>
  <div class="subscribe">
    <template v-if="!subscribeSuccessful">
      <input
          v-model="subscribeEmail"
          aria-label="Newsletter Subscription Email"
          placeholder="Your Email Here..."
          type="email"
          @keyup.enter="onSubscribe"
      />
      <CoreButton height="100%" @submit="onSubscribe">
        Subscribe
      </CoreButton>
    </template>
    <h3 v-else @click="subscribeSuccessful = false">
      Welcome! Check your email inbox to confirm your subscription. You champ.
    </h3>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "#imports";
import axios from "axios";

const subscribeEmail = ref("");
const subscribeSuccessful = ref(false);

const onSubscribe = async () => {
  if (subscribeEmail.value) {
    const formId = "3812335";

    const data = {
      api_key: "-OVn5y2IfE8cvsLo7gWF6Q",
      email: subscribeEmail.value
    };

    const url = `https://api.convertkit.com/v3/forms/${formId}/subscribe`;
    const result = await axios.post(url, data);

    if (result.data?.subscription?.id) {
      subscribeSuccessful.value = true;
    }
  }
};
</script>

<style lang="scss" scoped>
.subscribe {
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.25s ease;
  border-radius: var(--BorderRadius-L);
  grid-row: span 1;
  grid-template-columns: 3fr 1fr;
  grid-column: span 12;
  grid-gap: 0.6rem;

  input, button {
    height: 100%;
  }

  input {
    font-size: var(--FontSize-M);
    padding: 0 3rem;
    border-radius: var(--BorderRadius-L);
  }

  h3 {
    font-size: var(--FontSize-M);
    padding: 0 2rem;
    cursor: pointer;
    text-align: center;
    color: var(--Color-White);
    grid-column: span 2;
  }
}
</style>