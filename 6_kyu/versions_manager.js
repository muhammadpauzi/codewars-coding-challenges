/**
 * must use NODE v10
 * https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/javascript
 */

class VM {
    constructor(major, minor, patch) {
        this.rollbackVersions = [];
        this.version = { major, minor, patch };
    }

    major() {
        this.updateRollbackVersion();
        this.version.major += 1;
        this.version.minor = 0;
        this.version.patch = 0;
        return this;
    }

    minor() {
        this.updateRollbackVersion();
        this.version.minor += 1;
        this.version.patch = 0;
        return this;
    }

    patch() {
        this.handleDefaultPatch();
        this.updateRollbackVersion();
        this.version.patch += 1;
        return this;
    }

    rollback() {
        if (this.rollbackVersions.length === 0)
            throw new Error('Cannot rollback!');
        this.version = this.rollbackVersions[this.rollbackVersions.length - 1];
        this.rollbackVersions.pop();
        return this;
    }

    release() {
        this.handleDefaultPatch();
        const { major, minor, patch } = this.version;
        return [major, minor, patch].join('.');
    }

    // handle default value for patch
    handleDefaultPatch() {
        if (
            this.version.major === 0 &&
            this.version.minor === 0 &&
            this.version.patch === 0
        ) {
            this.version.patch = 1;
        }
    }

    updateRollbackVersion() {
        const { major, minor, patch } = this.version;
        this.rollbackVersions.push({ major, minor, patch });
    }
}

const vm = (version = '') => {
    // default value
    version += version.trim().length === 0 ? '0.0.0' : '.0.0.0';
    let versions = version
        .split('.')
        .filter((str) => str !== '')
        .slice(0, 3);
    // handle version is not number/decimal
    versions = versions.map((v) => {
        if (Number(v) != v)
            // means the version is include chars
            throw new Error('Error occured while parsing version!');
        return Number(v);
    });

    return new VM(versions[0], versions[1], versions[2]);
};

export { vm };
