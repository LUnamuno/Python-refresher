# 01 - Angular Like Button

**Codility:** [Angular Like Button](https://app.codility.com/programmers/trainings/8/angular_like_button/) - Exercise 8, Frontend - *easy*

Create a simple like button component with Angular 20.

## Task description

Build a like button component using Angular 20. Export the like button component as `LikeButtonComponent` (`export class LikeButtonComponent`).

### Requirements

**1. There should be a like button:**

- The content of the like button should be in the following format: `Like | 100`, where `100` is the total number of likes.
- It should have a `like-button` class.
- Wrap the number of likes in a `span` with a `likes-counter` class.
- The initial number of likes in the counter should be `100`.

**2. Users can add a like. By clicking the button:**

- The number of likes should increase by one.
- The like button should have the `liked` class in addition to the `like-button` class.

**3. Users can undo their like by clicking again on the button:**

- The counter should decrease by one.
- The `liked` class should be removed.

### Assessment / tools

- Design/styling is not assessed. Focus only on implementing the requirements.
- The "Preview" tab in Codility displays your component and can be used for testing.
- Language: TypeScript.

## Files

| File                                  | Purpose                                                                 |
|---------------------------------------|-------------------------------------------------------------------------|
| `README.md`                           | This description.                                                       |
| `package.json`                        | Node dependencies and scripts (the JavaScript counterpart of `requirements.txt`). |
| `jest.config.js`, `setup-jest.ts`     | Jest + `jest-preset-angular` configuration.                             |
| `tsconfig.json`, `tsconfig.spec.json` | TypeScript configuration for the component and the tests.               |
| `src/like-button.component.ts`        | The solution: the component to paste into Codility.                     |
| `src/like-button.component.spec.ts`   | Tests that encode the requirements above.                               |

This is a minimal setup for testing one component, not a full Angular CLI workspace.

## How to work

Node.js (LTS) is required. Check with `node --version`; if it is missing, install it from <https://nodejs.org> or with `winget install OpenJS.NodeJS.LTS`, then reopen the terminal.

```powershell
cd codility/exercise_8_frontend/01_angular_like_button
npm install
npm test
```

## Notes

- In Angular 20 components are standalone by default, so there is no `NgModule` and no `standalone: true` flag is needed.
- `[class.liked]="liked"` toggles the class while keeping the static `class="like-button"`.
- A template written on one line (`Like | <span ...>`) keeps the single space after the pipe, so `textContent` is exactly `Like | 100`.
- The tests call `fixture.detectChanges()` after each click: outside a real application nothing triggers change detection for you.

## Stretch goals

- Re-implement the state with Angular signals (`likes = signal(100)`, `liked = signal(false)`) and update the tests.
- Add an `@Input()` for the initial likes and an `@Output()` that emits the new total.
- Add `[attr.aria-pressed]` and test it.
