<template>
  <div id="Contact" class="container">
    <div class="contact__opening" v-if="!formType">
      <div class="contact-header">
        what can <span>the earth is square</span> do for you today?
      </div>
      <div class="contact-buttons">
        <span @click="goContactForm('work')">
          <CTAButton text="let's work together!"/>
        </span>
        <CTAButton text="please mentor me!"/>
      </div>
    </div>
    <div class="contact-form__wrapper" v-else-if="formType === 'work'">
      <form class="contact-form">
        <label for="Name">What is your name?</label>
        <input id="Name"/>
      </form>
    </div>
  </div>
</template>

<script>
import CTAButton from "../components/CTAButton"

export default {
  name: "Contact",
  components: {
    CTAButton
  },
  data() {
    return {
      formType: ''
    }
  },
  methods: {
    goContactForm(type) {
      this.formType = type
    }
  }
}
</script>

<style lang="scss" scoped>
#Contact {
  margin: auto;

  .contact__opening {
    .contact-header {
      text-align: center;
      font-weight: bold;
      font-size: 24px;
      margin-bottom: 60px;

      span {
        color: $rose;
      }
    }

    .contact-buttons {
      display: grid;
      grid-gap: 50px;
      grid-template: auto / 1fr 1fr;
    }
  }
}
</style>