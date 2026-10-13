# 02 - ReactLikeButton

**Codility:** [ReactLikeButton](https://app.codility.com/programmers/trainings/8/react_like_button/) - Exercise 8, Frontend - *easy*

Create a simple like button component with React.

## Task description

Build a "like button" component using React 16. The component should be the **default export** (`export default`).

### Requirements

**1. There should be a like button:**

- The content of the like button should be in the following format: `Like | 100`, where `100` is the total number of likes.
- It should have a `like-button` class.
- Wrap the number of likes in a `span` with a `likes-counter` class.
- The initial number of likes in the counter should be `100`.

**2. Users can add a like. By clicking the button:**

- The number of likes should increase by one.
- The like button should have the `liked` class in addition to the `like-button` class (you can use the `classnames` tool for that).

**3. Users can undo their like by clicking again on the button:**

- The counter should decrease by one.
- The `liked` class should be removed.

### Assessment / tools

- Only two imports are allowed: `react` (v16.8.6) and `classnames` (v2.2.5). Both are at the top of the starting code.
- Design/styling is not assessed. Focus only on implementing the requirements.
- The "Preview" tab in Codility displays your component and can be used for testing.

## Files

| File                     | Purpose                                                        |
|--------------------------|----------------------------------------------------------------|
| `README.md`              | This description.                                              |
| `package.json`           | Node dependencies and scripts (the JavaScript counterpart of `requirements.txt`). |
| `babel.config.js`        | Lets Jest understand modern JavaScript and JSX.                |
| `src/LikeButton.js`      | The solution: the component to paste into Codility.            |
| `src/LikeButton.test.js` | Tests that encode the requirements above.                      |

## How to work

Node.js (LTS) is required. Check with `node --version`; if it is missing, install it from <https://nodejs.org> or with `winget install OpenJS.NodeJS.LTS`, then reopen the terminal.

```powershell
cd codility/exercise_8_frontend/02_react_like_button
npm install
npm test
```

## Notes

- The code only uses `useState`, available since React 16.8, so it also runs on the Codility sandbox (React 16.8.6, classnames 2.2.5).
- `package.json` uses `react@^16.14` locally because the testing library needs the asynchronous `act` helper, added in 16.9. Nothing in the component depends on that.
- To undo a like use the *previous* state (`setLiked(prev => !prev)`). Deriving the counter from `liked` (`100 + (liked ? 1 : 0)`) is an alternative that cannot get out of sync.

## Stretch goals

- Take the initial count as a prop (`initialLikes`, default `100`) without breaking the default export.
- Add `aria-pressed` and test it.
- Disable double-activation while a (simulated) request is in flight.
