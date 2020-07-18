<template>
  <div id="Contact" class="container">
    <transition name="fade" mode="out-in">
      <div class="contact__opening" v-if="!formOpen" :key="'intro'">
        <div class="contact-header">
          what can <span>the earth is square</span> do for you today?
        </div>
        <div class="contact-buttons">
          <div class="contact-button" @click="goContactForm('work')">
            <CTAButton text="let's work together!"/>
          </div>
          <div class="contact-button">
            <CTAButton text="please mentor me!" disabled/>
          </div>
        </div>
      </div>
      <div class="contact-form__wrapper" v-else>
        <div class="contact-form__blurb">
          <div class="contact-form__blurb-header">
            <span>let's create something interesting</span>
          </div>
          <div class="contact-form__blurb-byline">
            Don't like forms? Send us an <span>email.</span>
          </div>
          <div class="contact-form__shapes">
            <img alt="Shapes" src="../assets/svg/contact-shapes.svg"/>
          </div>
        </div>
        <transition name="fade" mode="out-in">
          <router-view @submit="sendContactForm" v-if="!this.formSubmitted"/>
          <div class="contact-form__loading" v-else-if="this.submitting">
            <LoadingIcon message="Beaming message"/>
          </div>
          <div class="contact-form__success" v-else-if="this.submitSuccess">
            <font-awesome-icon icon="check-circle" size="4x"/>
            <span>Message sent!</span>
          </div>
        </transition>
      </div>
    </transition>
  </div>
</template>

<script>
import CTAButton from "../components/CTAButton"
import { createContactForm } from "../queries";
import LoadingIcon from "../components/LoadingIcon";

export default {
  name: "Contact",
  components: {
    LoadingIcon,
    CTAButton
  },
  data() {
    return {
      formOpen: !!this.$route.params.type,
      submitting: false,
      submitError: false,
      submitSuccess: false,
    }
  },
  watch: {
    $route(to) {
      this.formOpen = !!to.params.type
      this.submitError = false
      this.submitSuccess = false
    }
  },
  computed: {
    formSubmitted() {
      return this.submitError || this.submitSuccess || this.submitting
    }
  },
  methods: {
    goContactForm(type) {
      this.$router.push({ name: 'Contact Form', params: { type: type } })
      this.formOpen = true
    },
    sendContactForm(form) {
      this.submitting = true

      this.$axios({
        data: {
          query: createContactForm,
          variables: {
            name: form.name,
            email: form.email,
            message: form.message
          }
        }
      }).then(response => {
        this.submitting = false

        if (response.data.data.createContactForm.id) {
          this.submitSuccess = true
        } else {
          this.submitError = true
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
#Contact {
  padding-top: 50px;
  padding-bottom: 50px;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;

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
      justify-items: center;
    }
  }

  .contact-form__wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 50px;
    justify-items: center;
    height: 100%;
    box-sizing: border-box;
    align-items: center;

    .contact-form__blurb {
      .contact-form__blurb-header {
        margin-bottom: 40px;

        span {
          color: white;
          background-color: $rose;
          font-weight: 900;
          font-size: 38px;
          line-height: 1.5;
        }
      }

      .contact-form__blurb-byline {
        span {
          text-decoration: underline;
          cursor: pointer;
        }
      }

      .contact-form__shapes {
        padding-right: 50px;
        position: relative;
        margin-top: 50px;
      }
    }
  }

  .contact-form__loading {
    align-self: center;
  }

  .contact-form__success {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    span {
      margin-top: 50px;
      color: white;
      background-color: $rose;
      font-weight: 900;
      font-size: 38px;
    }
  }
}
</style>