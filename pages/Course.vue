<template>
  <div id="course">
    <CourseInformationSection/>

    <QuoteBreakSection/>

    <OutcomesSection/>

    <template v-if="isDesktop">
      <LearnSection/>

      <FAQSection/>

      <CTASection/>
    </template>
  </div>
</template>

<script lang="ts" setup>
import CourseInformationSection from "~/features/course/CourseInformationSection.vue";
import CTASection from "~/features/course/CTASection.vue";
import FAQSection from "~/features/course/FAQSection.vue";
import LearnSection from "~/features/course/LearnSection.vue";
import OutcomesSection from "~/features/course/OutcomesSection.vue";
import QuoteBreakSection from "~/features/course/QuoteBreakSection.vue";
import { useScreen } from "~/hooks/useScreen";

useSeoMeta({
  title: `Web Development Bootcamp - ${new Date().getFullYear()}`,
  description:
      `Join our Melbourne-based web development bootcamp and gain the skills needed for a
      successful career in this fast-paced industry. Our experienced instructors guide you through hands-on
      projects covering HTML, CSS, JavaScript, React, Node.js, and more. Flexible scheduling options available.
      Enroll now and start your journey towards a rewarding career in web development.`
});

const { isDesktop } = useScreen();
</script>

<style lang="scss" scoped>
#course {
  display: flex;
  flex-direction: column;
  margin-right: 0.6rem;
  gap: 0.6rem;
}
</style>