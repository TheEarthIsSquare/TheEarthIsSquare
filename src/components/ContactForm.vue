<template>
  <form class="contact-form" @submit.prevent="submitForm">
    <div class="contact-form__field" v-for="field in fields" :key="field.id">
      <label>
        <span>{{ field.label }}</span>
        <input :type="field.type" :placeholder="field.placeholder" v-model="form[field.id]" v-if="!field.textarea"/>
        <textarea rows="10" :type="field.type" :placeholder="field.placeholder" v-model="form[field.id]" v-else/>
      </label>
    </div>
    <button class="contact-form__submit" @click="submitForm">
      <span>let's get started</span>
      <font-awesome-icon icon="arrow-right"/>
    </button>
  </form>
</template>

<script>
export default {
  name: "ContactForm",
  data() {
    return {
      form: {},
      fieldsList: {
        'work': [
          {
            id: 'name',
            type: 'text',
            label: 'full name',
            placeholder: 'what should we call you?',
            textarea: false,
            vModel: 'clientName'
          },
          {
            id: 'email',
            type: 'email',
            label: 'email address',
            placeholder: 'where can we reach you?',
            textarea: false,
            vModel: 'clientEmail'
          },
          {
            id: 'message',
            type: 'text',
            label: 'your message',
            placeholder: 'get the conversation started...',
            textarea: true,
            vModel: 'clientMessage'
          },
        ]
      }
    }
  },
  computed: {
    type() {
      return this.$router.currentRoute.params.type
    },
    fields() {
      return this.fieldsList[this.type]
    }
  },
  methods: {
    submitForm() {
      this.$emit('submit', this.form)
    }
  },
  mounted() {
    this.form = {}
  }
}
</script>

<style lang="scss" scoped>
.contact-form {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;

  .contact-form__field {
    margin-bottom: 40px;

    &:last-child {
      margin-bottom: 0;
    }

    label {
      font-size: 16px;
      display: flex;
      flex-direction: column;

      span {
        font-weight: bold;
        margin-bottom: 5px;
      }

      input, textarea {
        font-family: 'Open Sans', sans-serif;
        font-size: 16px;
        color: white;
        padding: 15px 20px;
        background-color: #605F80;
        border: 2px solid #1C1A4B;
        border-radius: 10px;

        &::placeholder {
          color: white;
        }
      }
    }
  }

  .contact-form__submit {
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    background-color: $rose;
    padding: 15px 20px;
    color: white;
    border: none;
    border-radius: 10px;
    margin-left: auto;

    span {
      margin-right: 20px;
    }
  }
}
</style>