import { DropdownOption } from "~/components/CoreDropdown/CoreDropdown.types";

export type FormDataKeys = keyof typeof applyForm;
export const applyForm = reactive({
    firstName: '',
    lastName: '',
    email: '',

    bootcampProgram: '',
    codingLevel: '',
    graduationGoal: '',
    extraInfo: '',
    referralSource: '',

    subscribeToNewsletter: true,
    getInTouch: true,
});

export const getInputTitle = (key: FormDataKeys) => {
    return {
        "firstName": "First Name",
        "lastName": "Last Name",
        "email": "Email",
        "bootcampProgram": "Which program are you applying for?",
        "codingLevel": "Where do you see your current level of coding?",
        "graduationGoal": "What would you like to do after graduating?",
        "extraInfo": "Anything else you would like to let us know?",
        "referralSource": "How did you hear about The Earth Is Square?",
        "subscribeToNewsletter": "Yes, please keep me posted about upcoming events, discounts and more",
        "getInTouch": "I would like to learn more about The Earth Is Square. Please get in touch with me",
    }[key]
}

export const bootcampOptions: DropdownOption[] = [
    { label: 'Web Development Bootcamp: September 2023', value: 'September-23' }
];

export const codingLevelOptions: DropdownOption[] = [
    {
        label: 'Absolute Beginner - Spent less than 3 days trying to code.',
        value: 'Beginner'
    },
    {
        label: 'Making Progress - Programmed small loops and apps using tutorials of any language.',
        value: 'Making Progress'
    },
    {
        label: 'Intermediate - I can program and launch small apps on my own.',
        value: 'Intermediate'
    },
    {
        label: 'Professional - I am a CS graduate and/or a developer.',
        value: 'Professional'
    },
];

export const graduationOptions: DropdownOption[] = [
    {
        label: 'Get a better understanding of what code is like',
        value: 'Get a better understanding of what code is like'
    },
    {
        label: 'Work as a developer',
        value: 'Work as a developer'
    },
    {
        label: 'Start a company',
        value: 'Start a company'
    },
    {
        label: 'Communicate with or lead tech teams',
        value: 'Communicate with or lead tech teams'
    },
    {
        label: 'Other',
        value: 'Other'
    }
];

export const referralOptions: DropdownOption[] = [
    { label: 'Web search', value: 'Web search' },
    { label: 'Facebook', value: 'Facebook' },
    { label: 'Twitter', value: 'Twitter' },
    { label: 'LinkedIn', value: 'LinkedIn' },
    { label: 'Instagram', value: 'Instagram' },
    { label: 'Friends/Family', value: 'Friends/Family' },
    { label: 'Colleague', value: 'Colleague' },
    { label: 'Employer', value: 'Employer' },
    { label: 'Other', value: 'Other' },
];