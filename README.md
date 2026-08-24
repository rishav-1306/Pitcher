# 🚀 Automated Daily 3-Commit Contribution System for Pitcher

This repository is configured with a **GitHub Actions cloud workflow** that automatically makes **3 commits every day**, whether your local computer is **turned ON or OFF**.

---

## 🌟 How It Works (100% Automated Cloud Execution)

1. **GitHub Actions Schedule**: Runs automatically every day in GitHub's cloud using a cron schedule (`0 4 * * *` at 04:00 UTC / 09:30 AM IST).
2. **3 Separate Commits**: Each scheduled run appends entries to `logs/activity.log` and creates 3 individual timestamped commits.
3. **Heatmap Credit**: The commits are authored under your GitHub profile (`rishav-1306`), ensuring that all 3 daily contributions reflect directly on your GitHub activity heatmap.

---

## ⚙️ Mandatory One-Time Setup in GitHub

To allow GitHub Actions to push commits back to this repository, make sure the workflow has write permissions:

1. Go to your repository on GitHub: [`https://github.com/rishav-1306/Pitcher`](https://github.com/rishav-1306/Pitcher)
2. Click **Settings** (top navigation tab of your repository).
3. In the left sidebar, click **Actions** ➔ **General**.
4. Scroll down to the **Workflow permissions** section.
5. Select **"Read and write permissions"**.
6. Check the box **"Allow GitHub Actions to create and approve pull requests"**.
7. Click **Save**.

---

## 🕹️ Manual Trigger (Test Anytime)

You don't need to wait for the daily scheduled time to test it:
1. Go to the **Actions** tab on GitHub.
2. Select **"Daily Automated 3-Commits"** on the left menu.
3. Click the **Run workflow** dropdown button and click **Run workflow**.
4. Watch the 3 commits get added and pushed automatically in seconds!

---

## 💻 Optional Local Runner

If you ever want to create 3 commits locally from your machine:
```bash
python auto_commit.py
```
