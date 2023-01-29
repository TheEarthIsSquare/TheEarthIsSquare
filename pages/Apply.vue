<template>
  <div class="apply">
    <div v-if="!isSuccess" class="apply__inner-wrapper">
      <div class="apply__blurb">
        <Icon name="teis" size="8.5rem"/>
        <Heading type="h3">
          Ready for a good decision? Yay!<br/>
          We are excited to get to know you!
        </Heading>

        <Heading type="h5">
          Tell us a little bit about yourself, what you're interested in and how to get in touch with you.<br/>
          <br/>
          We will get back to you soon after and explain your options an potential next steps.<br/>
          Always feel free to contact us anytime if you have any questions.
        </Heading>
      </div>

      <form class="apply__form" @submit.prevent="submit">
        <div class="apply__header">
          <Heading type="h3">Application</Heading>
          <p>* Indicates Required</p>
        </div>

        <div class="apply__section">
          <div class="apply__section-heading">
            <h3>Personal Info</h3>
            <p>Help us get to know who you are and how to best contact you!</p>
          </div>

          <div class="apply__section-inputs">
            <div class="apply__section-inputs-row">
              <CoreInput
                  :label="getInputTitle('firstName')"
                  isRequired
                  @onChange="v => applyForm.firstName = v"
              />
              <CoreInput
                  v-if="isDesktop"
                  :label="getInputTitle('lastName')"
                  @onChange="v => applyForm.lastName = v"
              />
            </div>
            <div v-if="!isDesktop" class="apply__section-inputs-row">
              <CoreInput
                  :label="getInputTitle('lastName')"
                  @onChange="v => applyForm.lastName = v"
              />
            </div>
            <div class="apply__section-inputs-row">
              <CoreInput
                  :label="getInputTitle('email')"
                  isRequired
                  type="email"
                  @onChange="v => applyForm.email = v"
              />
            </div>
          </div>
        </div>

        <div class="apply__divider"/>

        <div class="apply__section">
          <div class="apply__section-heading">
            <h3>Course Application</h3>
            <p>Give us a better idea of your coding experience and expectations!</p>
          </div>

          <div class="apply__section-inputs">
            <div class="apply__section-inputs-row">
              <CoreDropdown
                  :options="bootcampOptions"
                  :title="getInputTitle('bootcampProgram')"
                  placement="bottom"
                  @onSelect="v => applyForm.bootcampProgram = v"
              />
            </div>

            <div class="apply__section-inputs-row">
              <CoreDropdown
                  :options="codingLevelOptions"
                  :title="getInputTitle('codingLevel')"
                  placement="bottom"
                  @onSelect="v => applyForm.codingLevel = v"
              />
            </div>

            <div class="apply__section-inputs-row">
              <CoreDropdown
                  :options="graduationOptions"
                  :title="getInputTitle('graduationGoal')"
                  placement="bottom"
                  @onSelect="v => applyForm.graduationGoal = v"
              />
            </div>

            <div class="apply__section-inputs-row">
              <CoreInput
                  label="Anything else you would like to let us know?"
                  @onChange="v => applyForm.extraInfo = v"
              />
            </div>

            <div class="apply__section-inputs-row">
              <CoreDropdown
                  :options="referralOptions"
                  :title="getInputTitle('referralSource')"
                  placement="bottom"
                  @onSelect="v => applyForm.referralSource = v"
              />
            </div>
          </div>
        </div>

        <div class="apply__divider"/>

        <div class="apply__form-footer">
          <CoreCheckbox
              :isChecked="applyForm.subscribeToNewsletter"
              :title="getInputTitle('subscribeToNewsletter')"
              label="Yes, please keep me posted about upcoming events, discounts and more."
              @onChange="v => applyForm.subscribeToNewsletter = v"
          />
          <CoreCheckbox
              :isChecked="applyForm.getInTouch"
              :title="getInputTitle('getInTouch')"
              label="I would like to learn more about The Earth Is Square. Please get in touch with me."
              @onChange="v => applyForm.getInTouch = v"
          />
          <CoreButton
              :isLoading="isLoading"
              height="4.8rem"
              variant="secondary"
              width="12rem"
          >
            {{ !isLoading ? "Let's Go!" : "" }}
          </CoreButton>
        </div>
      </form>
    </div>

    <div v-else class="apply__inner-wrapper">
      <div class="apply__blurb">
        <Icon name="teis" size="8.5rem"/>
        <h2>
          Successfully Submitted<br/>
          Congratulations!
        </h2>
        <h3>
          Wow, you've taken the first step to becoming a developer!<br/>
          <br/>
          We will be in contact as soon as possible to have a chat about your application, keep an eye out!
        </h3>

        <div class="apply__blurb-socials">
          <SocialIcon name="instagram" size="3.6rem"/>
          <SocialIcon name="twitter" size="3.6rem"/>
          <SocialIcon name="youtube" size="3.6rem"/>
          <SocialIcon name="linkedIn" size="3.6rem"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import CoreInput from "~/components/CoreInput.vue";
import CoreCheckbox from "~/components/CoreCheckbox.vue";
import axios from "axios";
import {
  applyForm,
  bootcampOptions,
  codingLevelOptions,
  getInputTitle,
  graduationOptions,
  referralOptions
} from "~/features/apply/apply.form";
import { useScreen } from "~/hooks/useScreen";

const { isDesktop } = useScreen();

const isLoading = ref(false);
const isSuccess = ref(false);

const router = useRouter();

const submit = () => {
  const nucleusUrl = process.env.NODE_ENV === 'development' ? 'http://localhost:4000/graphql' : 'https://nucleus.theearthissquare.com/graphql';

  if (!isLoading.value && !isSuccess.value) {
    isLoading.value = true;

    axios.post(nucleusUrl, {
      query: `query SendApplicationEmail($fields: [ApplicationField!]!, $subscribe: Boolean!) {sendApplicationEmail(fields: $fields, subscribe: $subscribe) }`,
      variables: {
        fields: Object.entries(applyForm).map(([key, value]) => ({
          label: getInputTitle(key as keyof typeof applyForm),
          value: String(value) === "true" ? "Yes" : String(value) === "false" ? "No" : value
        })),
        subscribe: applyForm.subscribeToNewsletter
      }
    }).then(result => {
      if (result) {
        isSuccess.value = true;
        router.push({ name: 'apply', query: { succeed: 'true' } });
      }
    }).finally(() => isLoading.value = false);
  }
}

</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

.apply {
  background-color: var(--Color-White);
  flex: 1;
  border-radius: var(--BorderRadius-L);
  padding: 10rem 0;

  @media screen and (max-width: $BreakPoint-Tablet) {
    padding: 5rem 0;
  }

  .apply__inner-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 5rem;
    max-width: var(--View-MaxWidth);
    margin: auto;
    height: 100%;

    .apply__blurb {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2rem;
      text-align: center;
      width: 100%;

      .apply__blurb-socials {
        display: flex;
        align-items: center;
      }

      h3 {
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
      }
    }

    .apply__form {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      gap: 5rem;

      @media screen and (max-width: $BreakPoint-Tablet) {
        padding: 0 2rem;
      }

      .apply__header {
        display: flex;
        justify-content: space-between;
        width: 100%;

        p {
          font-weight: var(--FontWeight-Bold);
        }
      }

      .apply__section {
        display: grid;
        grid-template-columns: 1fr 1fr;
        width: 100%;

        @media screen and (max-width: $BreakPoint-Tablet) {
          grid-template-columns: 1fr;
        }

        .apply__section-heading {
          display: flex;
          flex-direction: column;
          font-size: var(--FontSize-M);
        }

        .apply__section-inputs {
          display: flex;
          flex-direction: column;
          align-items: flex-end;
          gap: 2rem;
          padding-left: 5rem;

          @media screen and (max-width: $BreakPoint-Tablet) {
            padding-left: 0;
            align-items: center;
          }

          .apply__section-inputs-row {
            width: 100%;
            display: grid;
            grid-auto-columns: 1fr;
            grid-auto-flow: column;
            align-items: center;
            gap: 2rem;
          }
        }
      }

      .apply__divider {
        width: 100%;
        height: 0.3rem;
        background-color: var(--Color-Grey);
        border-radius: var(--BorderRadius-L);
      }

      .apply__form-footer {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100%;
        gap: 3rem;
      }
    }
  }
}
</style>